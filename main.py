import numpy as np
import json
import time
import sys
from rich.console import Console

console=Console()
def text_delay(text: str, style: str,end: int=0, delay: float=0.03):
    for char in text:
        console.print(char,end='',style=style)
        time.sleep(delay)
    if end==0: 
        print()

def Clear():
    try:
        file_path = "my_3d_data.json"
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        loaded_3d_array = np.array(data, dtype=object)
        demon_counts = [np.sum(array_2d[:, 0] == "-1") for array_2d in loaded_3d_array]
        mini = min(demon_counts)
        if mini > 0:
            new_3d_array = []
            for array_2d in loaded_3d_array:
                new_3d_array.append(array_2d[:-mini])
            loaded_3d_array = np.array(new_3d_array, dtype=object)
            data=loaded_3d_array.tolist()
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        pass

def Start(no_start=0):
    Clear()
    if no_start==1:
        console.print("--------------------------------------", style="yellow")
    text_delay("1. My Schedule",style="blue")
    text_delay("2. Create New",style="blue")
    text_delay("3. BYE",style="blue")
    while True:
        text_delay("Choice: ",style="blue", end=1) 
        choice=input()
        try:
            choice_int=int(choice)
            if choice_int==1:
                file_path = "my_3d_data.json"
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    My_sche(file_path)
                except Exception as e:
                    console.print("Schedule has not been created yet",style="red")
            elif choice_int==2:
                Create_new()
            elif choice_int==3:
                sys.exit()
            else:
                console.print("Error: choice",style="red")
        except ValueError:
            console.print("Error: no fault",style="red")
        time.sleep(0.5)

def My_sche(file_path):
    text_delay("1. Check",style="blue")
    text_delay("2. Delete",style="blue")
    text_delay("3. Edit",style="blue")
    text_delay("4. Cancel",style="blue")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    loaded_3d_array = np.array(data, dtype=object)
    while True:
        text_delay("Choice: ",style="blue", end=1) 
        choice=input()
        try:
            choice_int=int(choice)
            if choice_int==1:
                for i in range(loaded_3d_array.shape[0]):
                    console.print("--------------------------------------", style="white")
                    for j in range(loaded_3d_array.shape[1]):
                        if loaded_3d_array[i][j][0]!="-1":
                            console.print(f"{loaded_3d_array[i][j][0]} - {loaded_3d_array[i][j][1]}: {loaded_3d_array[i][j][2]}",style="red")
                console.print("--------------------------------------", style="white")
                time.sleep(0.5)
                My_sche(file_path) 
            elif choice_int==2:
                if loaded_3d_array.shape[0]==1:
                    Delete_sche_2D(file_path)
                Delete_sche(file_path)
            elif choice_int==3:
                text_delay("1. Edit",style="blue")
                text_delay("2. Swap",style="blue")
                #text_delay("3. Chance name",style="blue")
                text_delay("3. Cancel",style="blue")
                while True:
                    text_delay("Choice: ",style="blue", end=1) 
                    choice=input()
                    try:
                        choice_int=int(choice)
                        if choice_int==1:
                            Edit_3D(file_path)
                        elif choice_int==2:
                            if loaded_3d_array.shape[0]==1:
                                console.print("You have only 1 schedule",style="red")
                                time.sleep(0.5)
                            else:
                                for i in range(loaded_3d_array.shape[0]):
                                    console.print("--------------------------------------", style="white")
                                    console.print(f"{i+1}.",style="yellow")
                                    for j in range(loaded_3d_array.shape[1]):
                                        if loaded_3d_array[i][j][0]!="-1":
                                            console.print(f"{loaded_3d_array[i][j][0]} - {loaded_3d_array[i][j][1]}: {loaded_3d_array[i][j][2]}",style="red")
                                console.print("--------------------------------------", style="white")
                                while True:
                                    text_delay("Which (1): ",style="magenta", end=1)
                                    choice=input()
                                    try:
                                        choice_int_pick1=int(choice)
                                        if 0<choice_int_pick1<=loaded_3d_array.shape[0]:
                                            choice_int_pick1=choice_int_pick1-1
                                            for j in range(loaded_3d_array.shape[1]):
                                                if loaded_3d_array[choice_int_pick1][j][0]!="-1":
                                                    console.print(f"{loaded_3d_array[choice_int_pick1][j][0]} - {loaded_3d_array[choice_int_pick1][j][1]}: {loaded_3d_array[choice_int_pick1][j][2]}",style="red")
                                        else:
                                            console.print("Error: choice",style="red")
                                    except ValueError:
                                            console.print("Error: no fault",style="red")
                                    time.sleep(0.5)  

                                    text_delay("Which (2): ",style="magenta", end=1)
                                    choice=input()
                                    try:
                                        choice_int_pick2=int(choice)
                                        if 0<choice_int_pick2<=loaded_3d_array.shape[0]:
                                            choice_int_pick2=choice_int_pick2-1
                                            for j in range(loaded_3d_array.shape[1]):
                                                if loaded_3d_array[choice_int_pick2][j][0]!="-1":
                                                    console.print(f"{loaded_3d_array[choice_int_pick2][j][0]} - {loaded_3d_array[choice_int_pick2][j][1]}: {loaded_3d_array[choice_int_pick2][j][2]}",style="red")
                                            time.sleep(0.5) 
                                            break
                                        else:
                                            console.print("Error: choice",style="red")
                                    except ValueError:
                                            console.print("Error: no fault",style="red")
                                    time.sleep(0.5)  
                                text_delay("1. Swap",style="green")
                                text_delay("2. Cancel",style="green")
                                text_delay("Choice: ",style="blue", end=1) 
                                while True:
                                    choice=input()
                                    try:
                                        choice_int=int(choice)
                                        if choice_int==1:
                                            text_delay("Loading",style="white",end=1)
                                            text_delay("...",style="white",delay=0.5)
                                            swap_array=loaded_3d_array.copy()
                                            swap_array[choice_int_pick1], swap_array[choice_int_pick2]=loaded_3d_array[choice_int_pick2], loaded_3d_array[choice_int_pick1]
                                            data=swap_array.tolist()
                                            with open(file_path, 'w', encoding='utf-8') as f:
                                                json.dump(data, f, indent=4, ensure_ascii=False)
                                            console.print("->Success", style="green")
                                            My_sche(file_path)
                                        elif choice_int==2:
                                            My_sche(file_path)
                                        else:
                                            console.print("Error: choice",style="red")
                                    except ValueError:
                                            console.print("Error: no fault",style="red")
                                    time.sleep(0.5)  
                        # elif choice_int==3:
                        #     pass
                        elif choice_int==3:
                            Start(no_start=1)
                        else:
                            console.print("Error: choice",style="red")
                    except ValueError:
                        console.print("Error: no fault",style="red")
                    time.sleep(0.5)
            elif choice_int==4:
                Start(no_start=1)    
            else:
                console.print("\tError: choice",style="red")
        except ValueError:
            console.print("\tError: no fault",style="red")
        time.sleep(0.5)

def Delete_dirty_2D(array):
    for i in range(array.shape[0]-1,0,-1): #5->1
        if array[i][0]=="-1":
            array=np.delete(array, i, axis=0)
    if array.shape[0]==1:
        array=array.flatten()
    return array

def Edit_3D(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    loaded_3d_array = np.array(data, dtype=object)
    for i in range(loaded_3d_array.shape[0]):
        console.print("--------------------------------------", style="white")
        console.print(f"{i+1}.",style="yellow")
        for j in range(loaded_3d_array.shape[1]):
            if loaded_3d_array[i][j][0]!="-1":
                console.print(f"{loaded_3d_array[i][j][0]} - {loaded_3d_array[i][j][1]}: {loaded_3d_array[i][j][2]}",style="red")
    console.print("--------------------------------------", style="white")
    while True:
        text_delay("Which: ",style="magenta", end=1)
        choice=input()
        try:
            choice_int=int(choice)
            if 0<choice_int<=loaded_3d_array.shape[0]:
                choice_int=choice_int-1
                array=loaded_3d_array[choice_int]
                array=Delete_dirty_2D(array)
                Array_create(array, edit=1, choice_edit_3D=choice_int)
            else:
                console.print("Error: choice",style="red")
        except ValueError:
                console.print("Error: no fault",style="red")
        time.sleep(0.5)

def Delete_sche_2D(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    loaded_3d_array = np.array(data, dtype=object)
    console.print("--------------------------------------", style="white")
    for j in range(loaded_3d_array.shape[1]):
        if loaded_3d_array[0][j][0]!="-1":
            console.print(f"{loaded_3d_array[0][j][0]} - {loaded_3d_array[0][j][1]}: {loaded_3d_array[0][j][2]}",style="red")
    console.print("--------------------------------------", style="white")
    text_delay("1. Delete",style="blue")
    text_delay("2. Cancel",style="blue")
    while True:
        text_delay("Choice: ",style="blue", end=1) 
        choice=input()
        try:
            choice_int=int(choice)
            if choice_int==1:
                text_delay("...",style="red",delay=0.6,end=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    pass
                text_delay("Done",style="green")
                time.sleep(0.5)
                Start(no_start=1)
            elif choice_int==2:
                Start(no_start=1)
            else:
                console.print("Error: choice",style="red")
        except ValueError:
            console.print("Error: no fault",style="red")
        time.sleep(0.5)
    My_sche(file_path)

def Delete_sche(file_path):
    text_delay("1. Delete one",style="blue")
    text_delay("2. Delete all",style="blue")
    text_delay("3. Cancel",style="blue")
    while True:
        text_delay("Choice: ",style="blue", end=1) 
        choice=input()
        try:
            choice_int=int(choice)
            if choice_int==1:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                loaded_3d_array = np.array(data, dtype=object)
                for i in range(loaded_3d_array.shape[0]):
                    console.print("--------------------------------------", style="white")
                    console.print(f"{i+1}.",style="yellow")
                    for j in range(loaded_3d_array.shape[1]):
                        if loaded_3d_array[i][j][0]!="-1":
                            console.print(f"{loaded_3d_array[i][j][0]} - {loaded_3d_array[i][j][1]}: {loaded_3d_array[i][j][2]}",style="red")
                console.print("--------------------------------------", style="white")
                Delete_one(file_path,loaded_3d_array)
                Start()
            elif choice_int==2:
                text_delay("...",style="red",delay=0.6,end=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    pass
                text_delay("Done",style="green")
                time.sleep(0.5)
                Start()
            elif choice_int==3:
                Start(no_start=1)    
            else:
                console.print("\tError: choice",style="red")
        except ValueError:
            console.print("\tError: no fault",style="red")
        time.sleep(0.5)

def Delete_one(file_path, loaded_3d_array):
    while True:
        text_delay("Choice: ",style="blue", end=1) 
        choice=input()
        try:
            choice_int=int(choice)
            if 0<choice_int<=loaded_3d_array.shape[0]:
                choice_int=choice_int-1
                console.print("--------------------------------------", style="white")
                for j in range(loaded_3d_array.shape[1]):
                    if loaded_3d_array[choice_int][j][0]!="-1":
                        console.print(f"{loaded_3d_array[choice_int][j][0]} - {loaded_3d_array[choice_int][j][1]}: {loaded_3d_array[choice_int][j][2]}",style="red")
                console.print("--------------------------------------", style="white")
                loaded_3d_array = np.delete(loaded_3d_array, choice_int, axis=0)
                text_delay("...",style="white",delay=0.5)
                data=loaded_3d_array.tolist()
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                text_delay("Done",style="green")
                break
            else:
                console.print("Error: choice",style="red")
        except ValueError:
            console.print("Error: no fault",style="red")
        time.sleep(0.5)

def Time_begin_end():
    #begin
    text_delay("Time Begin {",style="yellow")
    while True:
        text_delay("\tHour: ","green", end=1)
        hour=input()
        try:
            hour_int_begin=int(hour)
            if 0 <= hour_int_begin < 24:
                break
            else:
                console.print("\tError: hour (0<=x<=23)",style="red")
        except ValueError:
            console.print("\tError: no fault",style="red")
        time.sleep(0.5)
    while True:
        text_delay("\tMinute: ","green", end=1)
        minute=input()
        try:
            minute_int_begin=int(minute)
            if 0<= minute_int_begin < 60:
                break
            else:
                console.print("\tError: minute (0<=x<=59)",style="red")
        except ValueError:
            console.print("\tError: no fault",style="red")
        time.sleep(0.5)
    text_delay("}",style="yellow")
    #end
    text_delay("Time End {",style="magenta")
    while True:
        while True:
            text_delay("\tHour: ","green", end=1)
            hour=input()
            try:
                hour_int_end=int(hour)
                if 0 <= hour_int_end < 24:
                    break
                else:
                    console.print("\tError: hour (0<=x<=23)",style="red")
            except ValueError:
                console.print("\tError: no fault",style="red")
            time.sleep(0.5)
        while True:
            text_delay("\tMinute: ","green", end=1)
            minute=input()
            try:
                minute_int_end=int(minute)
                if 0<= minute_int_end < 60:
                    break
                else:
                    console.print("\tError: minute (0<=x<=59)",style="red")
            except ValueError:
                console.print("\tError: no fault",style="red")
            time.sleep(0.5)
        if (hour_int_begin==hour_int_end and minute_int_begin<minute_int_end) or hour_int_begin<hour_int_end:
            break
        else:
            console.print("\tError: time begin > time end",style="red")
    text_delay("}",style="magenta")
    console.print("->Success", style="green")
    return hour_int_begin, minute_int_begin, hour_int_end, minute_int_end

def TODO():
    text_delay("TODO: ",style="cyan",end=1)
    todo=input()
    console.print("->Success", style="green")
    return todo

def Create_new():
    #begin_end
    hour_int_begin, minute_int_begin, hour_int_end, minute_int_end=Time_begin_end()
    #todo
    todo=TODO()
    Array(hour_int_begin, minute_int_begin, hour_int_end, minute_int_end, todo)

def Add_new_array(array, choice_edit_3D=-1):
    #begin_end
    hour_int_begin, minute_int_begin, hour_int_end, minute_int_end=Time_begin_end()
    #todo
    todo=TODO()
    Array(hour_int_begin, minute_int_begin, hour_int_end, minute_int_end, todo, array, choice_edit_3D)

def Edit_array(array, choice_edit_3D=-1):
    ndim=array.ndim
    if ndim==1:
        console.print("--------------------------------------", style="white")
        console.print(f"{array[0]} - {array[1]}: {array[2]}",style="red")
        console.print("--------------------------------------", style="white")
        text_delay("1. Time",style="blue")
        text_delay("2. Todo",style="blue")
        text_delay("3. All",style="blue")
        while True:
            text_delay("Choice: ",style="blue", end=1) 
            choice=input()
            try:
                choice_int=int(choice)
                if choice_int==1:
                    hour_int_begin, minute_int_begin, hour_int_end, minute_int_end=Time_begin_end()
                    array[0]=f"{hour_int_begin:02d}:{minute_int_begin:02d}"
                    array[1]=f"{hour_int_end:02d}:{minute_int_end:02d}"
                    break
                elif choice_int==2:
                    todo=TODO()
                    array[2]=todo
                    break
                elif choice_int==3:
                    hour_int_begin, minute_int_begin, hour_int_end, minute_int_end=Time_begin_end()
                    todo=TODO()
                    array[0]=f"{hour_int_begin:02d}:{minute_int_begin:02d}"
                    array[1]=f"{hour_int_end:02d}:{minute_int_end:02d}" 
                    array[2]=todo
                    break
                else:
                    console.print("Error: choice",style="red")
            except ValueError:
                console.print("Error: no fault",style="red")
            time.sleep(0.5)
        time.sleep(0.5)
    elif ndim==2:
        while True:
            console.print("--------------------------------------", style="white")
            for i in range(array.shape[0]):
                console.print(f"{i+1}. {array[i][0]} - {array[i][1]}: {array[i][2]}",style="red")
            console.print("--------------------------------------", style="white")
            text_delay("1. Choice",style="green")
            text_delay("2. Swap",style="green")
            text_delay("3. Save and quit",style="green")
            text_delay("Choice: ",style="blue", end=1) 
            choice=input()
            try:
                choice_int=int(choice)
                if choice_int==1:
                    while True:
                        text_delay("Which: ",style="magenta", end=1)
                        choice=input()
                        try:
                            choice_int_pick=int(choice)
                            if 0<choice_int_pick<=array.shape[0]:
                                console.print("--------------------------------------", style="white")
                                console.print(f"{array[choice_int_pick-1][0]} - {array[choice_int_pick-1][1]}: {array[choice_int_pick-1][2]}",style="red")
                                console.print("--------------------------------------", style="white")
                                text_delay("1. Time",style="blue")
                                text_delay("2. Todo",style="blue")
                                text_delay("3. All",style="blue")
                                while True:
                                    text_delay("Choice: ",style="blue", end=1) 
                                    choice=input()
                                    try:
                                        choice_int=int(choice)
                                        if choice_int==1:
                                            hour_int_begin, minute_int_begin, hour_int_end, minute_int_end=Time_begin_end()
                                            array[choice_int_pick-1][0]=f"{hour_int_begin:02d}:{minute_int_begin:02d}"
                                            array[choice_int_pick-1][1]=f"{hour_int_end:02d}:{minute_int_end:02d}"
                                            break
                                        elif choice_int==2:
                                            todo=TODO()
                                            array[choice_int_pick-1][2]=todo
                                            break
                                        elif choice_int==3:
                                            hour_int_begin, minute_int_begin, hour_int_end, minute_int_end=Time_begin_end()
                                            todo=TODO()
                                            array[choice_int_pick-1][0]=f"{hour_int_begin:02d}:{minute_int_begin:02d}"
                                            array[choice_int_pick-1][1]=f"{hour_int_end:02d}:{minute_int_end:02d}"
                                            array[choice_int_pick-1][2]=todo
                                            break    
                                        else:
                                            console.print("Error: choice",style="red")
                                    except ValueError:
                                        console.print("Error: no fault",style="red")
                                    time.sleep(0.5)
                                break
                            else:
                                console.print("Error: choice",style="red")
                        except ValueError:
                                console.print("Error: no fault",style="red")
                        time.sleep(0.5)    
                elif choice_int==2:
                    while True:
                        text_delay("Which (1): ",style="magenta", end=1)
                        choice=input()
                        try:
                            choice_int_pick1=int(choice)
                            if 0<choice_int_pick1<=array.shape[0]:
                                console.print(f"{array[choice_int_pick1-1][0]} - {array[choice_int_pick1-1][1]}: {array[choice_int_pick1-1][2]}",style="red")
                            else:
                                console.print("Error: choice",style="red")
                        except ValueError:
                                console.print("Error: no fault",style="red")
                        time.sleep(0.5)  

                        text_delay("Which (2): ",style="magenta", end=1)
                        choice=input()
                        try:
                            choice_int_pick2=int(choice)
                            if 0<choice_int_pick2<=array.shape[0]:
                                console.print(f"{array[choice_int_pick2-1][0]} - {array[choice_int_pick2-1][1]}: {array[choice_int_pick2-1][2]}",style="red")
                                time.sleep(0.5) 
                                break
                            else:
                                console.print("Error: choice",style="red")
                        except ValueError:
                                console.print("Error: no fault",style="red")
                        time.sleep(0.5)  
                    text_delay("1. Swap",style="green")
                    text_delay("2. Cancel",style="green")
                    text_delay("Choice: ",style="blue", end=1) 
                    while True:
                        choice=input()
                        try:
                            choice_int=int(choice)
                            if choice_int==1:
                                array[[choice_int_pick1-1, choice_int_pick2-1]] = array[[choice_int_pick2-1, choice_int_pick1-1]]
                                break
                            elif choice_int==2:
                                break
                            else:
                                console.print("Error: choice",style="red")
                        except ValueError:
                                console.print("Error: no fault",style="red")
                        time.sleep(0.5)  
                elif choice_int==3:
                    break
                else:
                    console.print("Error: choice",style="red")
            except ValueError:
                console.print("Error: no fault",style="red")
            time.sleep(0.5) 
        text_delay("Loading",style="white",end=1)
        text_delay("...",style="white",delay=0.5)
    if choice_edit_3D!=-1:
        Array_create(array, edit=1, choice_edit_3D=choice_edit_3D)
    else:    
        Array_create(array, edit=1)

def Array(hour_int_begin, minute_int_begin, hour_int_end, minute_int_end, todo, array=None, choice_edit_3D=-1):
    text_delay("Loading",style="white",end=1)
    text_delay("...",style="white",delay=0.5)
    console.print("->Success", style="green")
    if array is not None:
        text_delay("Adding",style="white",end=1)
        text_delay("...",style="white",delay=0.5)
        console.print("->Success", style="green")
        add_array=np.array([f"{hour_int_begin:02d}:{minute_int_begin:02d}", f"{hour_int_end:02d}:{minute_int_end:02d}", todo])
        array=np.vstack([array,add_array])
        console.print("--------------------------------------", style="white")
        for i in range(array.shape[0]):
            print(f"{array[i][0]} - {array[i][1]}: {array[i][2]}")
        console.print("--------------------------------------", style="white")
    else:
        array=np.array([f"{hour_int_begin:02d}:{minute_int_begin:02d}", f"{hour_int_end:02d}:{minute_int_end:02d}", todo])
        console.print("--------------------------------------", style="white")
        print(f"{hour_int_begin:02d}:{minute_int_begin:02d} - {hour_int_end:02d}:{minute_int_end:02d}: {todo}")
        console.print("--------------------------------------", style="white")
    time.sleep(0.5)
    Array_create(array, choice_edit_3D=choice_edit_3D)

def Array_create(array, edit=0, choice_edit_3D=-1):
    file_path = "my_3d_data.json"
    if edit==1:
        ndim=array.ndim
        if ndim==1:
            console.print("--------------------------------------", style="white")
            print(f"{array[0]} - {array[1]}: {array[2]}")
            console.print("--------------------------------------", style="white")
        elif ndim==2:
            console.print("--------------------------------------", style="white")
            for i in range(array.shape[0]):
                print(f"{array[i][0]} - {array[i][1]}: {array[i][2]}")
            console.print("--------------------------------------", style="white")
    text_delay("1. Save",style="blue")
    text_delay("2. Edit",style="blue")
    text_delay("3. Delete",style="blue")
    text_delay("4. Create more",style="blue")
    while True:
        text_delay("Choice: ",style="blue", end=1) 
        choice=input()
        try:
            choice_int=int(choice)
            if choice_int==1:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if array.ndim==1:
                        array=np.vstack((array, ["-1","-1","-1"]))
                    array=array[np.newaxis, :, :]
                    array_data=np.array(data, dtype=object)
                    if array.shape[1]>array_data.shape[1]:
                        number=array.shape[1]-array_data.shape[1]
                        for i in range(number):
                            list_2D_slices=[]
                            for slice_2D in array_data:
                                m_slice_2D=np.vstack((slice_2D, ["-1","-1","-1"]))
                                list_2D_slices.append(m_slice_2D)
                            array_data=np.stack(list_2D_slices, axis=0)
                    elif array.shape[1]<array_data.shape[1]:
                        number=array_data.shape[1]-array.shape[1]
                        for i in range(number):
                            list_2D_slices=[]
                            for slice_2D in array:
                                m_slice_2D=np.vstack((slice_2D, ["-1","-1","-1"]))
                                list_2D_slices.append(m_slice_2D)
                            array=np.stack(list_2D_slices, axis=0)
                    if choice_edit_3D!=-1:
                        array_data[choice_edit_3D]=array
                    else:
                        array_data=np.concatenate((array_data, array), axis=0)
                    text_delay("Loading",style="white",end=1)
                    text_delay("...",style="white",delay=0.5)
                    data=array_data.tolist()
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    console.print("->Success", style="green")
                except Exception as e:
                    text_delay("Loading",style="white",end=1)
                    text_delay("...",style="white",delay=0.5)
                    if array.ndim==1:
                        array=np.vstack((array, ["-1","-1","-1"]))
                    array=array[np.newaxis, :, :]
                    data=array.tolist()
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    console.print("->Success", style="green")
                Clear()
                Start(no_start=1)
            elif choice_int==2:
                if choice_edit_3D!=-1:
                    Edit_array(array, choice_edit_3D)
                else:
                    Edit_array(array)
            elif choice_int==3:
                ndim=array.ndim
                if ndim==1:
                    text_delay("...",style="red",delay=0.5,end=1)
                    if choice_edit_3D!=-1:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        loaded_3d_array = np.array(data, dtype=object)
                        loaded_3d_array = np.delete(loaded_3d_array, choice_edit_3D, axis=0)
                        data=loaded_3d_array.tolist()
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                    text_delay("Done",style="red")
                    time.sleep(0.5)
                    Start()
                elif ndim==2:
                    console.print("--------------------------------------", style="white")
                    for i in range(array.shape[0]):
                        console.print(f"{i+1}. {array[i][0]} - {array[i][1]}: {array[i][2]}",style="red")
                    console.print("--------------------------------------", style="white")
                    text_delay("1. Delete All: ",style="blue") 
                    text_delay("2. Delete one: ",style="blue") 
                    text_delay("3. Cancel ",style="blue") 
                    text_delay("Choice: ",style="blue", end=1) 
                    while True:
                        choice=input()
                        try:
                            choice_int=int(choice)
                            if choice_int==1:
                                text_delay("...",style="red",delay=0.6,end=1)
                                if choice_edit_3D!=-1:
                                    with open(file_path, 'r', encoding='utf-8') as f:
                                        data = json.load(f)
                                    loaded_3d_array = np.array(data, dtype=object)
                                    loaded_3d_array = np.delete(loaded_3d_array, choice_edit_3D, axis=0)
                                    data=loaded_3d_array.tolist()
                                    with open(file_path, 'w', encoding='utf-8') as f:
                                        json.dump(data, f, indent=4, ensure_ascii=False)
                                text_delay("Done",style="green")
                                Start()
                            elif choice_int==2:
                                while True:
                                    text_delay("Which: (0 to cancel) ",style="magenta", end=1)
                                    choice=input()
                                    try:
                                        choice_int_pick=int(choice)
                                        if 0<choice_int_pick<=array.shape[0]:
                                            console.print(f"{array[choice_int_pick-1][0]} - {array[choice_int_pick-1][1]}: {array[choice_int_pick-1][2]}", style="red")
                                            time.sleep(0.8)
                                            text_delay("...",style="red",delay=0.6,end=1)
                                            array = np.delete(array, choice_int_pick-1, axis=0)
                                            if array.shape[0]==1:
                                                array=array.flatten()
                                            text_delay("Done",style="green")
                                            time.sleep(0.5)
                                            break
                                        elif choice_int_pick==0:
                                            break
                                        else:
                                            console.print("Error: choice",style="red")
                                    except ValueError:
                                            console.print("Error: no fault",style="red")
                                    time.sleep(0.5) 
                                break
                            elif choice_int==3:
                                break
                            else:
                                console.print("Error: choice",style="red")
                        except ValueError:
                            console.print("Error: no fault",style="red")
                        time.sleep(0.5)
                if choice_edit_3D!=-1:
                    Array_create(array, edit=1, choice_edit_3D=choice_edit_3D)
                else:    
                    Array_create(array, edit=1)
            elif choice_int==4:
                Add_new_array(array, choice_edit_3D=choice_edit_3D)
            else:
                console.print("Error: choice (1,2)",style="red")
        except ValueError:
            console.print("Error: no fault",style="red")
        time.sleep(0.5)
if __name__=="__main__":
    Start()
    # my_3d_array = np.array([
    #     [[1, 2, 3],
    #     [4, 5, 6]],

    #     [[10, 11, 12],
    #     [13, 14, 15]],

    #     [["Hàng A", "Dữ liệu A.1", "Dữ liệu A.2"],
    #     ["Hàng B", "Dữ liệu B.1", "Dữ liệu B.2"]]
    # ], dtype=object)
    # array=my_3d_array[0]
    # print(array)
    
    # existing_3d_array = np.array([
    #     [[1, 2, 3],
    #     [4, 5, 6]],

    #     [[10, 11, 12],
    #     [13, 14, 15]]
    # ])
    #existing_3d_array[0], existing_3d_array[1]=existing_3d_array[1], existing_3d_array[0]
    # existing_3d_array = existing_3d_array[[1, 0]]
    # print(existing_3d_array)
    # new_2d_array_to_add = np.array([
    #     [20, 21, 22],
    #     [23, 24, 25],
    #     [23, 24, 25]
    # ])

    # new_2d_array_to_add_expanded = new_2d_array_to_add[np.newaxis, :, :]
    
    
    # list_of_modified_2d_slices = []
    # for slice_2d in existing_3d_array:
    #     modified_slice_2d = np.vstack((slice_2d, [-1,-1,-1]))
    #     list_of_modified_2d_slices.append(modified_slice_2d)
    # existing_3d_array = np.stack(list_of_modified_2d_slices, axis=0)

    # existing_3d_array = np.concatenate(
    # (existing_3d_array, new_2d_array_to_add_expanded),
    # axis=0)

    # data_to_save = new_2d_array_to_add_expanded.tolist()
    # print(data_to_save)
    # file_path = "my_3d_data.json"
    # with open(file_path, 'w', encoding='utf-8') as f:
    #     json.dump(data_to_save, f, indent=4, ensure_ascii=False)
    # try:
    #     with open(file_path, 'r', encoding='utf-8') as f:
    #         data = json.load(f)
    #     loaded_3d_array = np.array(data, dtype=object)
    #     print(loaded_3d_array)
    #     print(type(loaded_3d_array))

    #     if loaded_3d_array[0][0][0]==-1:
    #         print("hel")
    #     # print()
    #     # for i in range(loaded_3d_array.shape[0]):
    #     #     print(loaded_3d_array[i])
    #     #     print("----------")
    # except Exception as e:
    #     print(f"Một lỗi không mong muốn đã xảy ra")
    