from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime, timedelta

def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY")

def is_valid_score(score):
    """Check if score is numeric or valid format"""
    return score.isdigit() or (score.startswith(('ET', 'PEN')) and '-' in score)

def scrape_date(date_str):
    url = f"https://www.yallakora.com/match-center/مركز-المباريات?date={date_str}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Extract actual match date from dayName
    day_name_div = soup.find('div', class_='dayName')
    match_day = day_name_div.find('span').text.strip() if day_name_div else date_str
    
    match_cards = soup.find_all('div', class_='matchCard')
    matches = []
    
    for card in match_cards:
        # League name
        league = card.find('h2').text.strip() if card.find('h2') else 'غير متوفر'
        
        # Team names
        teams = card.find_all('p', limit=2)
        team1 = teams[0].text.strip() if len(teams) > 0 else 'غير متوفر'
        team2 = teams[1].text.strip() if len(teams) > 1 else 'غير متوفر'
        
        # Match result
        mresult = card.find('div', class_='MResult')
        result = 'لم تبدأ'
        if mresult:
            scores = mresult.find_all('span', class_='score')
            if len(scores) >= 2:
                score1 = scores[0].text.strip()
                score2 = scores[1].text.strip()
                
                if is_valid_score(score1) and is_valid_score(score2):
                    result = f"{score1}-{score2}"
                else:
                    # Handle special cases like postponed matches
                    status = mresult.find('span', class_='status')
                    if status:
                        result = status.text.strip()
                    else:
                        result = 'غير معروف'
        
        # Match time
        time_span = mresult.find('span', class_='time') if mresult else None
        time = time_span.text.strip() if time_span else 'غير متوفر'
        
        # Match type
        type_div = card.find('div', class_='date')
        type_of_match = type_div.text.strip() if type_div else 'غير متوفر'
        
        matches.append({
            'الدوري': league,
            'الفريق الأول': team1,
            'الفريق الثاني': team2,
            'الوقت': time,
            'نوع المباراة': type_of_match,
            'تاريخ المباراة': match_day,
            'النتيجة': result
        })
    
    print(f"📅 تم معالجة {date_str}: {len(matches)} مباراة")
    return matches

def main():
    start_date = get_valid_date("أدخل تاريخ البدء (MM/DD/YYYY): ")
    end_date = get_valid_date("أدخل تاريخ الانتهاء (MM/DD/YYYY): ")
    
    if start_date > end_date:
        start_date, end_date = end_date, start_date
        print("تم تبديل التواريخ: تاريخ البدء كان بعد تاريخ الانتهاء")

    all_matches = []
    current_date = start_date

    while current_date <= end_date:
        date_str = current_date.strftime("%m/%d/%Y")
        all_matches += scrape_date(date_str)
        current_date += timedelta(days=1)

    if all_matches:
        filename = f"مباريات_{start_date.strftime('%d-%m')}_{end_date.strftime('%d-%m')}.csv"
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=all_matches[0].keys())
            writer.writeheader()
            writer.writerows(all_matches)
        print(f"\n✅ تم جمع {len(all_matches)} مباراة بنجاح. البيانات في: {filename}")
    else:
        print("❌ لم توجد مباريات في الفترة المحددة")

if __name__ == "__main__":
    main()
