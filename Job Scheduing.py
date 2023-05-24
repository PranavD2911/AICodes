def job_scheduling(jobs):
    # Sort the jobs in non-decreasing order of their durations
    sorted_jobs = sorted(jobs, key=lambda x: x[1])

    schedule = []  # List to store the scheduled jobs

    for job in sorted_jobs:
        start_time = 0
        if schedule:
            # Calculate the start time for the current job
            start_time = schedule[-1][2] + schedule[-1][1]

        schedule.append((job[0], job[1], start_time))

    return schedule


# Take input from the user
n = int(input("Enter the number of jobs: "))
jobs = []

for i in range(n):
    job_id = input("Enter job ID for job {}: ".format(i + 1))
    duration = int(input("Enter duration for job {}: ".format(i + 1)))
    jobs.append((job_id, duration))

# Call the job_scheduling function to get the schedule
schedule = job_scheduling(jobs)

# Print the schedule
print("Job Schedule:")
for job in schedule:
    print("Job ID: {}, Start Time: {}, End Time: {}".format(job[0], job[2], job[2] + job[1]))
