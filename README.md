# wake-up
专注语音唤醒


### 安装依赖

```bash
sudo apt-get update -y
sudo apt-get install portaudio19-dev python3-pyaudio sox pulseaudio libsox-fmt-all ffmpeg
pip3 install pyaudio
```

```bash
git clone https://ghproxy.com/https://github.com/shaonianzhentan/wake-up

cd wake-up

pip3 install -r requirements.txt
```

### 安装 swig
```bash
cd $HOME
wget https://wzpan-1253537070.cos.ap-guangzhou.myqcloud.com/misc/swig-3.0.10.tar.gz
tar xvf swig-3.0.10.tar.gz
cd swig-3.0.10
sudo apt-get -y update
sudo apt-get install -y libpcre3 libpcre3-dev
./configure --prefix=/usr --without-clisp --without-maximum-compile-warnings
make
sudo make install
sudo install -v -m755 -d /usr/share/doc/swig-3.0.10
sudo cp -v -R Doc/* /usr/share/doc/swig-3.0.10
sudo apt-get install -y libatlas-base-dev
```

### 构建 snowboy

```bash
cd $HOME
wget https://wzpan-1253537070.cos.ap-guangzhou.myqcloud.com/wukong/snowboy.tar.bz2
tar -xvjf snowboy.tar.bz2
cd snowboy/swig/Python3
make
cp _snowboydetect.so wake-up的根目录/snowboy/
```

### 运行
```bash
python3 wake.py
```

## 相关文档

自定义唤醒词
- https://snowboy.hahack.com/

核心代码来自于`wukong-robot`
- https://wukong.hahack.com/