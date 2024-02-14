#!/bin/usr/python3
""" Medicine progress"""
from datetime import datetime, timedelta

class Medicine():
    def __init__(self, med_type, issue_duration):
        self.med_type = med_type
        self.date_given = datetime.utcnow()
        self.duration = issue_duration
        self.med_end = self.date_given + timedelta(days=self.duration)
        
if __name__ == "__main__":
    med_type = input("Medicine Issued: ")
    duration = int(input("Medication Duration (days): "))
    
health = Medicine(med_type, duration)
print("medication data saved!")
print("Medicine Type:", health.med_type)
print("Date Given:", health.date_given)
print("Duration:", health.duration, "days")
print("Medication End Date:", health.med_end)