# LBYL approach
def safe_devide_1(x, y):
    if y == 0:
        print("Divide by 0 attempt detected.")
        return None
    return x / y

# EAFP approach (Easier to Ask for Forgiveness than Permission)
def safe_devide_2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Divide by 0 attempt detected.")
        return None
    

# LBYL approach example
def save_a_file():
    result = save_prefs()
    if result == 'error':
        print("Preference not saved.")
        return
    result = save_text()
    if result == 'error':
        print("Not enough memory.")
        return
    result = save_format()
    if result == 'error':
        print("Format not saved.")
        return
    

# EAFP approach example 較簡單的寫法
def save_a_file():      # 先執行，再處理錯誤
    try:
        save_prefs()
        save_text()
        save_format()
    except:
        print("Something went wrong...")
        return

    
def save_prefs():
    return 'error'

def save_text():
    return 'error'

def save_format():
    return 'error'