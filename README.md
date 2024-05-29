# USB Charger DIY (USB 充电器 DIY)

[中文说明](#chinese)

![](001.webp)


USB charger DIY, using fast charging module, detects charging voltage, current, power, temperature, capacity etc. Programming with micropython.

This project is to provide a reference prototype, you can add or delete functions according to your own ideas to DIY more interesting projects.

PCB design using the software of LICAD, the microcontroller program using micropython.

<font color=red>**Please pay attention to safety during DIY due to the presence of 220V voltage.**</font>

## Components

- **Fast charging module**. 
- **MCU**, ESP32S2 mini development board. 
- **Current sensor**, INA219 module. 
- **Temperature sensor**, NTC, MF58 thermistor (3950, 10K). 
- **OLED**, 128x32, I2C interface. 
- **Power supply**, DC/5V module. 
- **Buzzer**, Passive buzzer. 
- **Photoresistor**, optional. 
- **LED**, three color co-positive LED.

### cost 
- Fast charging module: $0.2-$0.5 
- ESP32S2 mini: $1.5-$2 
- INA219: $0.7-$0.9 
- NTC: $0.02 
- OLED (128x32): $1-$1.2 
- 5V power module: $0.3-$0.5 
- buzzer: $0.1 
- LED: $0.02 
- Photoresistor: 0.1 yuan 
- Other: $1-$2 

Total: About $5-$6.

## schematic diagram

![](sch.png)

## Project link: 
- Project
    - [github](https://github.com/shaoziyang/USBChargerDIY)
    - [gitee](https://gitee.com/shaoziyang/usb-charger-diy)
- [EEWorld activity stickers](https://bbs.eeworld.com.cn/search.php?mod=forum&api=yes&searchsubmit=yes&kw=%A1%BEUSB%B3%E4%B5%E7%C6%F7DIY%A1%BF)
- [LCEDA Design Documents](https://oshwhub.com/shao.ziyang/USB_Charge_DIY_V2)
- [Material Selection Table 【 Tencent Document 】](https://docs.qq.com/sheet/DZXRCeWhxc0VWbFZu)
- [micropython](https://micropython.org)


---

## <a id="chinese"></a>说明

**USB 充电器 DIY**，使用网络上低成本的快充模块，加上MCU和传感器，实现电压、电流、功率、温度等参数采集，可以监测充电状态，统计充电容量等功能。

本项目是为了提供一个可以参考的原型，大家可以在此基础上，增加或删除功能，按照自己想法DIY出更多有趣的制作。

PCB设计使用了立创EDA软件，单片机程序使用 micropython 开发。

<font color=red>**因为存在220V高压，DIY时请注意安全。**</font>


## 主要器件

为了简化DIY的复杂度，主要元件使用了模块，其它元件数量也尽可能少。

- **快充模块**。型号众多，成本较低，18W的居多（5V3.4A、9V2A、12V1.5A），可以根据需要选择。因为快充模块质量参差不齐，采购时尽量选择评价较高的，使用前需要多测试（注意安全），确认没有问题后在使用。
- **MCU**：ESP32S2 mini开发板（可以使用其它型号）。使用ESP32S2，一个是支持micropython；其次因为性价比高，还支持网络，缺点是不支持蓝牙。
- **电流传感器**：INA219模块。第一版时使用了霍尔型的ACS712电流传感器，第二版改为INA219。
- **温度传感器**：MF58热敏电阻（3950，10K）。监测充电过程中内部温度，在温度过高时可以提示。
- **OLED**：128x32，I2C 接口。
- **电源**：DC/5V模块。用于将快充模块的输出电压转换为5V。部分快充模块输出是高压，部分会动态调整输出电压，因此需要使用一个单独的DC5V模块。如果快充模块带有单独的USB 5V输出口（非快充口），则可以省略此模块。
- **蜂鸣器**：无源蜂鸣器（注意不要使用有源蜂鸣器）。用于发出提示声音。
- **光敏电阻**（可选），用于采集环境光线亮度，用于动态调整LED输出亮度，避免晚上时LED太亮刺眼。
- **LED**：三色共阳LED，用于指示充电状态。第一版时使用了WS2812B。原理图中此处存在一个bug，不应该将电阻连接到公共阳极端，而是每个LED的负极单独串联一个电阻，这样三个LED就互不影响（因为各LED的导通电压不同）。

### 大致成本

- 快充模块：1-3元
- MCU（ESP32S2开发板）：10元
- 电流传感器（INA219）：4元
- 温度传感器（NTC）：0.1元
- OLED（128x32）：7元
- 5V电源模块：2元
- 无源蜂鸣器：0.2元
- LED：0.1元
- 光敏电阻：0.1元
- 外壳（塑料盒）：1-2元
- 其它（电源线、导线、热缩套管、螺丝、尼龙螺柱）：5元
- 总计：约30元


## 制作步骤

- 首先选择需要的器件、辅助材料等。
- 根据快充模块和其它元件大小、安装位置，确定外壳尺寸。
- 制作外壳，使用3D打印机打印外壳，或者使用其它方式制作外壳。
- 设计PCB板，打样并焊接元件。
- 调试硬件，确定各部分工作正常。
- 将快充模块的功率电感输出高压端引线取下，连接到INA219的IN+，INA219的IN-用导线连接到原电感输出端，也就是将INA219串联到电感输出回路中。
- 将快充模块和其它元件固定到外壳中。
    - 安装前先测试快充模块，确定功能和功率都是正常的，避免安装后不能使用。
- 编写MCU程序。
- 测试程序，确认功能正常。
- 完成DIY，开始使用。

### 工具

- 热熔胶
- 电烙铁
- 剪刀
- 电动螺丝刀
- 钻头


## 原理图

![](sch.png)


## 代码

程序使用micropython编写，使用asyncio实现多任务。asyncio 部分使用了作者的另外一个开源 **SAPF**（[Simple Asynchronous Program Framework for micropython](https://github.com/shaoziyang/SimpleAsynchronousProgramFramework)），用以简化程序结构。

OLED 部分使用了社区的 mpy-lib 驱动中的 [I2C OLED ASCII display drive](https://github.com/micropython-Chinese-Community/mpy-lib/tree/master/LED/OLED_I2C_ASC)，使用了8x16点阵字体。

### 程序文件：

- main.py，主程序文件，用以启动SAPF。
- sapfmain.py，SAPF主程序。
- sapf_cfg.py，任务配置文件。
- gv.py，公共变量和函数
- board.py，板级驱动文件
- pins.py，引脚配置
- cfg.py，参数配置
- task_main.py，初始化、采样任务
- display.py，显示、触摸键、LED显示任务
- lib，驱动库文件夹
    - oled.py，OLED驱动
    - Font_6x8.py，字体文件
    - Font_8x16.py
    - Font_12x24.py
    - Font_16x32.py
    - ina219.py，INA219驱动

### 程序功能说明

上电后先检查 I2C 设备地址。如果地址不正确，将闪红色LED，程序死循环。

然后启动各相关任务。
- main() 任务定期采样（100ms），并判断是否处于充电状态。如果在充电状态，则累计充电时间和充电功率。
- show_info() 任务每秒刷新一次，显示总线电压、电流、温度、功率等参数。
    - 显示持续60秒后关闭OLED屏。
    - 当按下触摸键、充电开始、充电结束时自动打开 OLED。
- task_LED() 任务以不同颜色的LED，指示充电功率。
    - 小于0.3W时为未充电状态，显示绿色呼吸灯。
    - 小于2W时为小功率模式，显示黄色呼吸灯。
    - 小于6W时为中功率模式，显示橙色呼吸灯。
    - 大于6W时为大功率模式，显示红色呼吸灯。
    - 为了避免夜晚时 LED 刺眼，会自动根据环境光强度调整 LED 亮度。
- task_TP() 任务检测触摸键。

## 相关链接

- 项目网址：
    - [github](https://github.com/shaoziyang/USBChargerDIY)
    - [gitee](https://gitee.com/shaoziyang/usb-charger-diy)
- [EEWorld活动贴](https://bbs.eeworld.com.cn/search.php?mod=forum&api=yes&searchsubmit=yes&kw=%A1%BEUSB%B3%E4%B5%E7%C6%F7DIY%A1%BF)
- [立创EDA设计文件](https://oshwhub.com/shao.ziyang/USB_Charge_DIY_V2)
- [物料选型表【腾讯文档】](https://docs.qq.com/sheet/DZXRCeWhxc0VWbFZu)
- [micropython](https://micropython.org)
