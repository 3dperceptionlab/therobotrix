// Fill out your copyright notice in the Description page of Project Settings.

#include "Tracker.h"

#include "EngineUtils.h" 

// Sets default values
ATracker::ATracker()
{
	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	PrimaryActorTick.bStartWithTickEnabled = true;
	m_frame = 0;
	m_record = false;
}

// Called when the game starts or when spawned
void ATracker::BeginPlay()
{
	Super::BeginPlay();

	EnableInput(GetWorld()->GetFirstPlayerController());
	UInputComponent* myInputComp = this->InputComponent;
	if (myInputComp)
		SetupMyPlayerInputComponent(myInputComp);
}

// Called every frame
void ATracker::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	if (m_record)
	{
		FString tick_string_ = "frame\r\n";

		float time_ = UGameplayStatics::GetRealTimeSeconds(GetWorld());
		FString time_string_ = FString::SanitizeFloat(time_ * 1000.0f);
		//FFileHelper::SaveStringToFile(time_string_ + "\r\n", *m_absolute_file_path, FFileHelper::EEncodingOptions::AutoDetect, &IFileManager::Get(), EFileWrite::FILEWRITE_Append);
		tick_string_ += time_string_ + " " + FString::FromInt(m_frame) + "\r\n";
		m_frame++;

		if (GEngine)
		{
			FVector camera_location_ = GEngine->GetFirstLocalPlayerController(GetWorld())->PlayerCameraManager->GetCameraLocation();
			FRotator camera_rotation_ = GEngine->GetFirstLocalPlayerController(GetWorld())->PlayerCameraManager->GetCameraRotation();

			FString camera_string_ = "Camera " + camera_location_.ToString() + " " + camera_rotation_.ToString();
			//FFileHelper::SaveStringToFile(camera_string_ + "\r\n", *m_absolute_file_path, FFileHelper::EEncodingOptions::AutoDetect, &IFileManager::Get(), EFileWrite::FILEWRITE_Append);
			tick_string_ += camera_string_ + "\r\n";

			//GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Yellow, "Camera " + camera_location_.ToString() + " " + camera_rotation_.ToString());
		}

		std::set<FString> actor_names_;

		for (TObjectIterator<AStaticMeshActor> Itr; Itr; ++Itr)
		{
			FString actor_name_ = Itr->GetName();

			if (actor_names_.find(actor_name_) == actor_names_.end())
			{
				actor_names_.insert(actor_name_);

				FVector actor_location_ = Itr->GetActorLocation();
				FRotator actor_rotation_ = Itr->GetActorRotation();
				FBox actor_bbox_ = Itr->GetComponentsBoundingBox();
				FVector actor_bbox_max_ = actor_bbox_.Max;
				FVector actor_bbox_min_ = actor_bbox_.Min;

				FString actor_string_ = actor_name_ + " " + actor_location_.ToString() + " " + actor_rotation_.ToString() + " " + actor_bbox_max_.ToString() + " " + actor_bbox_min_.ToString();
				//FFileHelper::SaveStringToFile(actor_string_ + "\r\n", *m_absolute_file_path, FFileHelper::EEncodingOptions::AutoDetect, &IFileManager::Get(), EFileWrite::FILEWRITE_Append);
				tick_string_ += actor_string_ + "\r\n";

				//GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Yellow, Itr->GetName() + " " + actor_location_.ToString() + " " + actor_rotation_.ToString());
			}
		}

		(new FAutoDeleteAsyncTask<FMyTaskName>(tick_string_, m_absolute_file_path))->StartBackgroundTask();
	}
}

void ATracker::SwitchRecord()
{
	m_record = !m_record;
}

void ATracker::SetupMyPlayerInputComponent(UInputComponent* myInputComponent)
{
	myInputComponent->BindAction("SwitchRecord", EInputEvent::IE_Pressed, this, &ATracker::SwitchRecord);
}