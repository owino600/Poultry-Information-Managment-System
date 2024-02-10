#!/bin/usr/python3
""" Medicine progress"""
from datetime import datetime

class Medicine():
    def __init__(self, med_type, issue_date, issue_duration, issue_complete):
        self.med_type = med_type
        self.date_given = datetime.utcnow()
        self.duration = issue_duration
        self.med_end = issue_complete
        
if __name__ == "__main__":
    med_type = input("Medicine Issued: ")
    date_given = input("Date of issue: ")
    duration = input("Medication Duration: ")
    med_end = input("Medication Complete date: ")
        
    health = Medicine(med_type, date_given, duration, med_end)
    print("medication data saved!")