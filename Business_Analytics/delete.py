Query#1:
SELECT
    Artist.Name AS ArtistName,
    COUNT(PlaylistTrack.PlaylistId) AS PlaylistCount
FROM
    Artist
JOIN
    Album ON Artist.ArtistId = Album.ArtistId
JOIN
    Track ON Album.AlbumId = Track.AlbumId
JOIN
    PlaylistTrack ON Track.TrackId = PlaylistTrack.TrackId
GROUP BY
    Artist.ArtistId
ORDER BY
    PlaylistCount DESC
LIMIT 5;


Query#2:
WITH CustomerFirstPurchase AS (
    SELECT
        i.CustomerId,
        MIN(i.InvoiceDate) AS FirstPurchaseDate
    FROM
        Invoice i
    GROUP BY
        i.CustomerId
),
CustomerSecondPurchase AS (
    SELECT
        i.CustomerId,
        MIN(i.InvoiceDate) AS SecondPurchaseDate
    FROM
        Invoice i
    WHERE
        i.InvoiceDate > (
            SELECT FirstPurchaseDate
            FROM CustomerFirstPurchase cf
            WHERE cf.CustomerId = i.CustomerId
        )
    GROUP BY
        i.CustomerId
),
TimeToSecondPurchase AS (
    SELECT
        c.CustomerId,
        julianday(cs.SecondPurchaseDate) - julianday(cf.FirstPurchaseDate) AS DaysToSecondPurchase
    FROM
        CustomerFirstPurchase cf
    JOIN
        CustomerSecondPurchase cs ON cf.CustomerId = cs.CustomerId
    JOIN
        Invoice i ON cs.CustomerId = i.CustomerId
    JOIN
        Customer c ON i.CustomerId = c.CustomerId
)
SELECT
    g.Name AS Genre,
    AVG(ttsp.DaysToSecondPurchase) AS AvgDaysToSecondPurchase
FROM
    Track t
JOIN
    Genre g ON t.GenreId = g.GenreId
JOIN
    InvoiceLine il ON t.TrackId = il.TrackId
JOIN
    TimeToSecondPurchase ttsp ON il.InvoiceId = ttsp.CustomerId
WHERE
    g.Name IN ('Rock', 'Pop')
GROUP BY
    g.Name;



Query#3:
WITH AlbumTrackSales AS (
    SELECT
        al.Title AS AlbumTitle,
        ar.Name AS ArtistName,
        COUNT(il.TrackId) AS TracksSold
    FROM
        InvoiceLine il
    JOIN
        Track t ON il.TrackId = t.TrackId
    JOIN
        Album al ON t.AlbumId = al.AlbumId
    JOIN
        Artist ar ON al.ArtistId = ar.ArtistId
    GROUP BY
        al.Title, ar.Name
)
SELECT
    AlbumTitle,
    ArtistName,
    TracksSold
FROM
    AlbumTrackSales
ORDER BY
    TracksSold DESC
LIMIT 10;



Query#4:
SELECT
    MediaType.Name AS MediaTypeName,
    COUNT(Track.TrackId) AS TrackCount
FROM
    MediaType
JOIN
    Track ON MediaType.MediaTypeId = Track.MediaTypeId
GROUP BY
    MediaType.MediaTypeId
ORDER BY
    TrackCount DESC
LIMIT 5;
