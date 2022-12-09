from execution_timer import ExecutionTimer


timer = ExecutionTimer()

x = 0
for i in range(1000000000):
    x += i

timer.completed()

print('Execution time:', timer.execution_time)