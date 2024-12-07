import pyaudio

pa = pyaudio.PyAudio()

for i in range(pa.get_device_count()):
    info = pa.get_device_info_by_index(i)
    print(f"Device {i} : {info['name']}")
    print(f" Default Sample Rate : {info['defaultSampleRate']}")
    print(f"MAx input channels : {info['maxInputChannels']}")
    print(f"Max Output channels : {info['maxOutputChannels']}")
