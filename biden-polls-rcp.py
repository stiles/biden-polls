#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Get latest Biden trends from Real Clear Politics

url = "https://www.realclearpolitics.com/epolls/other/president-biden-job-approval-7320.html#polls"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X "}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

tables = soup.findAll("table", attrs={"class": "data"})

src = pd.read_html(str(tables))[0]

latest_df = src[:1].copy()

latest_df.columns = latest_df.columns.str.lower()

latest_df[["begin", "end"]] = (
    latest_df["date"].astype(str).str.split(" - ", n=1, expand=True)
)

date = (latest_df["end"] + "/2021").astype(str)

latest_df["date"] = pd.to_datetime(date).dt.date

latest_df.drop(["poll", "sample", "begin", "end"], axis=1, inplace=True)

latest_df.head()

# Import historical polling average for Biden from RCP via Wayback Machine

historical = pd.read_csv("data/processed/biden_history.csv")

historical.drop(["wayback_date", "wayback_time"], axis=1, inplace=True)

# Append latest to historical

full_df = historical.append(latest_df).reset_index(drop=True)

full_df["date"] = pd.to_datetime(full_df["date"])

full_df = full_df.sort_values("date", ascending=False)

full_df["candidate"] = "President Biden"

full_df['spread'] = full_df['spread'].round(2)

full_df.to_csv('data/processed/biden_polling_averages.csv', index=False)