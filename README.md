# Biden Polls
Tracking President Biden's polling averages from [Real Clear Politics](https://www.realclearpolitics.com/epolls/other/president-biden-job-approval-7320.html#polls) since inauguration via the Wayback Machine.

A Github action runs the scrape at Noon and 6 p.m. Pacific time each day and, if there's new data, appends it to the [historical timeseries](https://github.com/stiles/biden-polls/blob/main/data/processed/biden_polling_averages.csv). It also sends an email notifying me about the action. 
