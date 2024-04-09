import os

local_parametr = os.getenv('LOCAL_START')

if local_parametr is not None:
    print(f"Значення змінної оточення LOCAL_START: {local_parametr}")
else:
    print("Змінна оточення LOCAL_START не встановлена.")
