# Excel_Statistics：Statistical functions that cannot be achieved with EXCEL,Make statistics simpler

<div align="center">
<img src="https://raw.githubusercontent.com/wuxingyu090/excel_statistics/main/src/excel.png" align="center" style="width: 100%" />
</div>
<br>

Excel is a very convenient data text, but its table filtering cannot satisfy everyone. I want to develop a tool that is more convenient to use to count Excel data.

## Features

***

- 🧠Easy to use and fast.
- The matching method is scalable.
- You can count different tables in batches.
- 👩‍🎨👩🏼‍💻👩🏼‍🎓Wide range of applications.

## News

***

- 1 May 2024

  :

  - Fuzzy matching through statistical configuration tables support
  - Independent specific matching support
  - Chart display support

## Commands

***

- `--show` – show Parameters, default False, do not directly output the chart

## Setup

Environmental preparation:

* Install the Git tool in advance, and the latest version is enough.
* Install the Python environment in advance, preferably the V3.10 version

1. Get Clone the project

2. Prepare tables that require statistics, Put it into the main directory of the project

3. Open config-keycount.xlsx under the input directory. Refer to Sheet<count_rule> to write statistical rules, which can be written in multiple copies. After editing, **replace the Sheet name with the 'rule_table_list' list in the main.py file.**

   ```python
   def run(show):
       rule_table_list = ['count_rule', 'count_rule1', 'count_rule2'] #Replace this list
       config_keycount = 'config-keycount'
   ```

   

4. 🔥 And now **run**:

   ```bash
   pip install -r requirements.txt
   python main.py  #Python Version 3.10.6
   ```

   

## ❤️ Top donations

***

You can be in this list:

1. Mrs Hby. Donation: **10$** (!!!)

## Contributors

***

- Main contributor: @Josiah Wu

