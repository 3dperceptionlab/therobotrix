// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include <set>

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Engine/StaticMeshActor.h"
#include "Kismet/GameplayStatics.h"
#include "Tracker.generated.h"

UCLASS()
class HAMBURGHAUS_API ATracker : public AActor
{
	GENERATED_BODY()

public:
	// Sets default values for this actor's properties
	ATracker();
	void SwitchRecord();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:
	// Called every frame
	virtual void Tick(float DeltaTime) override;
	void SetupMyPlayerInputComponent(UInputComponent* myInputComponent);

private:
	FString m_save_directory = FString("D:/datasetvr-tools");
	FString m_file_name = FString("scene.txt");
	FString m_absolute_file_path = m_save_directory + "/" + m_file_name;
	unsigned long int m_frame;
	bool m_record;
};

class FMyTaskName : public FNonAbandonableTask
{
	friend class FAutoDeleteAsyncTask<FMyTaskName>;

public:
	FMyTaskName(FString str, FString absoluteFilePath) :
		m_str(str),
		m_absolute_file_path(absoluteFilePath)
	{}

protected:
	FString m_str;
	FString m_absolute_file_path;

	void DoWork()
	{
		// Place the Async Code here.  This function runs automatically.
		FFileHelper::SaveStringToFile(m_str, *m_absolute_file_path, FFileHelper::EEncodingOptions::AutoDetect, &IFileManager::Get(), EFileWrite::FILEWRITE_Append);
	}

	// This next section of code needs to be here.  Not important as to why.

	FORCEINLINE TStatId GetStatId() const
	{
		RETURN_QUICK_DECLARE_CYCLE_STAT(FMyTaskName, STATGROUP_ThreadPoolAsyncTasks);
	}
};