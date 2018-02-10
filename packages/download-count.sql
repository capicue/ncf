SELECT file.project as name, count(*) as downloads
    FROM [the-psf:pypi.downloads20180209]
    GROUP BY name
    ORDER BY downloads DESC
    LIMIT 10000
