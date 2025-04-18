class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def shortest_job_next(process_list):
    process_list.sort(key=lambda p: (p.arrival_time, p.burst_time))  # Sort by arrival, then burst (FCFS if same burst)
    ready_queue = []
    time = 0
    completed_processes = []
    
    while process_list or ready_queue:
        # Add processes that have arrived to the ready queue
        while process_list and process_list[0].arrival_time <= time:
            ready_queue.append(process_list.pop(0))
        
        if ready_queue:
            ready_queue.sort(key=lambda p: (p.burst_time, p.arrival_time))  # SJN: Shortest Burst First, FCFS tie-breaker
            current_process = ready_queue.pop(0)
            time += current_process.burst_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed_processes.append(current_process)
        else:
            time += 1  # If no process is ready, increment time
    
    # Print results
    print("\n--- Shortest Job Next Scheduling ---\n")
    print("Gantt Chart:")
    print(" -> ".join([f"P{p.pid}" for p in completed_processes]))
    
    print("\nProcess Metrics:")
    print("PID\tTAT\tWT")
    total_tat, total_wt = 0, 0
    for p in completed_processes:
        print(f"P{p.pid}\t{p.turnaround_time}\t{p.waiting_time}")
        total_tat += p.turnaround_time
        total_wt += p.waiting_time
    
    print("\nTotal Turnaround Time:", total_tat)
    print("Average Turnaround Time:", round(total_tat / len(completed_processes), 2))
    print("Total Waiting Time:", total_wt)
    print("Average Waiting Time:", round(total_wt / len(completed_processes), 2))

# User input
num_processes = int(input("Enter the number of processes (3-10): "))
processes = []

for i in range(num_processes):
    arrival_time = int(input(f"Enter Arrival Time for Process {i}: "))
    burst_time = int(input(f"Enter Burst Time for Process {i}: "))
    priority = int(input(f"Enter Priority for Process {i}: "))
    processes.append(Process(i, arrival_time, burst_time, priority))

shortest_job_next(processes)
