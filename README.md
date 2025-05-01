

```markdown
# Yallakora Match Scraper 📅⚽

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## What does it do?  
Scrape football match data from [Yallakora](https://www.yallakora.com) including:  
- Match dates & times  
- Teams & leagues  
- Scores/results  
- Match types (friendly, league, etc.)  
- Export to **CSV** with Arabic headers  

---

## Requirements ⚙️  
1. Python 3.7+  
2. Install dependencies:  
   ```bash
   pip install requests beautifulsoup4
   ```

---

## How to Use 🚀  
1. **Run the script**:  
   ```bash
   python scraper.py
   ```

2. **Enter dates** when prompted:  
   ```  
   Enter start date (MM/DD/YYYY): 08/01/2023  
   Enter end date (MM/DD/YYYY): 08/05/2023  
   ```

3. **Check output**:  
   - CSV file created: `مباريات_01-08_05-08.csv`  
   - Contains columns:  
     ```  
     الدوري | الفريق الأول | الفريق الثاني | الوقت | نوع المباراة | تاريخ المباراة | النتيجة  
     ```

---

## Example Output 📊  
| الدوري       | الفريق الأول | الفريق الثاني | الوقت   | نوع المباراة | تاريخ المباراة | النتيجة |  
|--------------|-------------|--------------|---------|-------------|---------------|---------|  
| الدوري المصري | الأهلي      | الزمالك      | 8:00 PM | مباراة رسمية | 01/08/2023    | 2-1     |  

---

## Important Notes ⚠️  
- **Respect website policies**: Check Yallakora's `robots.txt` and terms of service.  
- **Rate limiting**: Add `time.sleep()` between requests if blocked.  
- **Anti-scraping measures**: May break if site adds CAPTCHA or changes HTML structure.  

---

## Contributing 💡  
1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/cool-update`)  
3. Commit changes (`git commit -m 'Add cool feature'`)  
4. Push to branch (`git push origin feature/cool-update`)  
5. Open a pull request  

---

## License 📜  
[MIT License](LICENSE) - Copyright (c) 2023 [Your Name]  
```

### What to add to your repository:  
1. Create a `LICENSE` file (choose MIT or another license).  
2. Add a sample CSV output file (e.g., `sample_output.csv`).  
3. Include a `.gitignore` file for Python:  
   ```  
   # Python  
   __pycache__/  
   *.pyc  
   *.pyo  
   *.pyd  
   .Python  
   ``` 
