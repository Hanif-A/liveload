import time

max_seconds = 60

for loop_num in range(1, max_seconds):

    print_passed = '#' * loop_num
    print_remain = '-' * (max_seconds-loop_num)

    print(print_passed+print_remain, end='\r')
    time.sleep(1)

# Clear when done
print(' ' * max_seconds, end='\r')
