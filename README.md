# 🖥️ Web Scraping Remote Jobs

This project scrapes a list of **remote jobs** from web3.career using **scrapy**.

## 🚀 **Features**
✅ Web scraping for remote jobs and its salary from web3.career  
✅ Saves data to **JSON** format  

## 📂 **Project Structure**
- 📂 **web-scraping-remote-job**
    - 📜 **README.md** → Project description
    - 📜 **requirements.txt** → Dependencies for the project
    - 📂 **jobscraper** → Main project folder
        - 📂 **data**
            - 📜 **data.json** → Scraped data
        - 📂 **jobscraper**
            - 📂 **spiders** → Scrapy spiders
                - 📜 **jobspider.py** → Spider for scraping job data
            - 📜 **items.py** → Define data structure for scraped items
            - 📜 **middlewares.py** → Custom middlewares
            - 📜 **pipelines.py** → Data processing pipelines
            - 📜 **settings.py** → Scrapy project settings

### 🔧 Installation  
1️⃣ Clone the repository  
```bash
git clone https://github.com/rakaaksara62/remote-job-scraper.git
cd remote-job-scraper
```
2️⃣ Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
## 📊 How to Run
```bash
cd jobscraper
scrapy crawl jobspider -O data/output.json
```

💡 Have questions or feedback? Feel free to reach out!
📧 Email: raka.khairann@gmail.com
