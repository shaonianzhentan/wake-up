
do_not_bother = False
is_recordable = True

def setRecordable(value):
    """设置是否可以开始录制语音"""
    global is_recordable
    is_recordable = value

def isRecordable():
    """是否可以开始录制语音"""
    global is_recordable
    return is_recordable

def is_proper_time():
    """是否合适时间"""
    global do_not_bother
    if do_not_bother == True:
        return False
    return True