import signal
from snowboy import snowboydecoder

class WakeUp():
  
    def __init__(self):
        self.interrupted = False
        signal.signal(signal.SIGINT, self.signal_handler) # 捕获ctrl+c

        model = '萝卜头.pmdl'
        self.detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5) # 设置语音模型与敏感度
        print('Listening... Press Ctrl+Z to exit')
        
    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def detected_callback(self):
        print('叮')

    def audio_recorder_callback(self, fp, callback=None):
        print(fp)
        print('咚')

    # 启动机器人
    def run(self):
        self.detector.start(
              detected_callback=self.detected_callback, 
              audio_recorder_callback=self.audio_recorder_callback,
              interrupt_check=self.interrupt_callback,
              silent_count_threshold=15,
              recording_timeout=5 * 4,
              sleep_time=0.03)

WakeUp().run()