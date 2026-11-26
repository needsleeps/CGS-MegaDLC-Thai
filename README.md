# CGS Mega DLC — ภาษาไทย (Thai Translation)

ม็อดแปลภาษาไทยสำหรับเนื้อหาที่ม็อด [CGS Mega DLC (THE MOST COMPLETE MOD)](https://steamcommunity.com/sharedfiles/filedetails/?id=2661428590) เพิ่มเข้ามาใน City Game Studio รวม 493 ข้อความ ได้แก่ ธีมเกม คำวิจารณ์ของนิตยสาร อีเวนต์สุ่ม ฟีเจอร์เอนจิน ฟีเจอร์ร้านค้าดิจิทัล ระดับความยาก และชื่อแผนที่

> งานแปลแฟนเมด ไม่ใช่ของทางการ และไม่มีไฟล์ของ CGS Mega DLC อยู่ใน repo นี้

## สิ่งที่ต้องมี

- เกม City Game Studio และม็อด **CGS Mega DLC**
- (แนะนำ) [City Game Studio — ภาษาไทย](https://github.com/needsleeps/CityGameStudio-Thai) สำหรับแปลตัวเกมหลัก

ม็อดนี้ใส่คำแปลให้ทั้งภาษา **ไทย (NeedSleep)** ของม็อดแปลตัวเกม และภาษา **ไทย** ที่มากับเกม จึงใช้คู่กับภาษาไทยแบบไหนก็ได้

## วิธีใช้

1. เปิดใช้ม็อดในเมนู **Mods** พร้อมกับ CGS Mega DLC (ตอนนี้ยังไม่ได้ลง Steam Workshop ให้ใช้วิธีสร้างม็อดจากโฟลเดอร์ด้านล่าง)
2. เลือกภาษาไทยในเมนูภาษา

ถ้าจะใช้ไฟล์จาก repo นี้โดยตรง ให้เปิดเกม ไปที่ **Mods → สร้างม็อดใหม่** แล้วเลือกโฟลเดอร์ `mod/`

## ข้อจำกัดที่รู้อยู่

- **ชื่อแพลตฟอร์ม ชิ้นส่วนเครื่อง บริษัท บุคคล และชื่อเกมจริง คงเป็นภาษาอังกฤษ** เพราะเกมไม่ส่งชื่อพวกนี้ผ่านระบบแปล และเป็นชื่อเฉพาะอยู่แล้ว
- **ข้อความยาว 30 ข้อความยังเป็นภาษาอังกฤษ** (รีวิวและอีเวนต์ที่ยาวเกิน 128 ตัวอักษร) เพราะระบบม็อดของเกมจำกัดความยาวคีย์ไว้ที่ 128 ตัวอักษร และ Mega DLC ใช้ข้อความอังกฤษทั้งประโยคเป็นคีย์ คำแปลของข้อความกลุ่มนี้เก็บไว้ที่ `translation/not_shipped_long_keys.json` เผื่อวันหนึ่งข้อจำกัดนี้ถูกยก
- ถ้า Mega DLC แก้ข้อความอังกฤษแม้ตัวอักษรเดียว ข้อความนั้นจะกลับเป็นอังกฤษจนกว่าจะอัปเดตคำแปลตาม

## โครงสร้าง

| ที่อยู่ | คืออะไร |
|---|---|
| `mod/` | โฟลเดอร์ม็อดพร้อมใช้ |
| `translation/megadlc_th.json` | คำแปลแบบ `ข้อความอังกฤษ: ข้อความไทย` — แก้คำแปลที่ไฟล์นี้ |
| `translation/not_shipped_long_keys.json` | คำแปลของข้อความที่ยาวเกินข้อจำกัดของเกม (ไม่ได้ใส่ในม็อด) |
| `GLOSSARY.md` | อภิธานศัพท์ชุดเดียวกับม็อดแปลตัวเกม |
| `tools/build.py` | ประกอบ `mod/mod.json` จากไฟล์คำแปล |

แก้คำแปลแล้วรัน `python tools/build.py` เพื่อประกอบม็อดใหม่

## English

Thai translation of the text added by the CGS Mega DLC mod (themes, magazine review lines, events, engine and store features). Requires CGS Mega DLC. Platform, company and person names are not translatable through the game's mod system and stay in English; 30 lines longer than the game's 128-character key limit are not shipped.

## สัญญาอนุญาต

สคริปต์ใช้ MIT ส่วนคำแปลและเอกสารใช้ CC BY 4.0 ดู [LICENSE](LICENSE) CGS Mega DLC เป็นผลงานของผู้สร้างม็อดต้นฉบับ
