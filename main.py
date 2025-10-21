import datetime, bday_messages as bd

today = datetime.date.today()
hashtag_festival = datetime.date(2025, 10, 18)

days_prior = hashtag_festival - today

if today == hashtag_festival: print(bd.random_message())
else: print(f'It has been {abs(days_prior)} days since the hashtag festival 2025')