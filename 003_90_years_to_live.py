your_age = input("Enter your current age (years): ")
wife_age = input("Enter your wife's age (years): ")

your_life = 90 - int(your_age)
wife_life = 90 - int(wife_age)

your_month = your_life * 12
wife_month = wife_life * 12

your_week = your_life * 52
wife_week = wife_life * 52

your_day = your_life * 365
wife_day = wife_life * 365

month_together = your_month if your_month < wife_month else wife_month
day_together = your_day if your_day < wife_day else wife_day
week_together = your_week if your_week < wife_week else wife_week


print(
    "If you and your wife both live for 90 years,\n"
    f"You have {your_day} days or {your_week} weeks or {your_month} months left.\n"
    f"Your wife has {wife_day} days or {wife_week} weeks or {wife_month} months left.\n"
    f"You and your wife can live together for {day_together} days or {week_together} weeks or {month_together} months"
)