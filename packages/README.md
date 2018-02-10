# Python Package Guide

When choosing which packages to use, there are a few things to keep in mind to save you time and frustration in the future. An ideal package is:

1. **Popular**: Tracking down bugs in a package is a huge time sink. Choosing packages with lots of users increases your chances of being able to easily google errors.
2. **Actively Developed**: It sucks spending time learning to use a package just to find out it doesn't have a feature you need or is broken in some way. If a package is being actively developed there's a good chance of fixing it instead of having to jump ship.
3. **Mature**: If a package is older there's been more time for pain points to be fixed in response to user feedback.

Look for a high number of downloads, frequent releases, and a resonable creation date.

## Popularity

In the following steps we'll create a spreadsheet of the top 10,000 most popular Python packages with descriptions.

[Google's BigQuery](https://bigquery.cloud.google.com/table/the-psf:pypi.downloads) has a database containing a row for every download of a Python package. From the website, we can run the query in [`download-count.sql`](packages/download-count.sql) to create a csv file containing package names and download counts.

The code in [`get-descriptions.py`](packages/get-descriptions.py) fetches descriptions for each package and finally writes the result to `packages.csv`.
