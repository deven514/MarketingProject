# This file contains all the Stored Procedures to get the data

CREATE PROCEDURE SelectAllBrands()
BEGIN
    Select brand_id, brand_name from sentiment_analysis.brands order by brand_id;
end;

CREATE PROCEDURE SelectAllData()
BEGIN
    select sno, asin, brand_id, rating,  cleaned_review_text from reviews where cleaned_review_text is not null;
end;

CREATE PROCEDURE  SelectReviewsByASIN(IN amazonNo varchar(10))
BEGIN
    Select products.title, reviews.rating, reviews.cleaned_review_text, sentiment_score from products, reviews
    Where reviews.asin = products.asin
    and reviews.asin = amazonNo;
END;



CREATE PROCEDURE SelectByBrand(In brand text)
BEGIN
    SELECT reviews.asin, title, rating, cleaned_review_text, sentiment_score from reviews, brands, products
    WHERE brands.Brand_Id = reviews.Brand_Id
    AND brands.Brand_Id = products.Brand_Id
    AND brands.brand_name = brand
    AND cleaned_review_text is NOT NULL
    ORDER BY asin;
end;



CREATE PROCEDURE SelectAllBrandNames()
BEGIN
    Select brand_name from brands order by brand_name;
end;


CREATE PROCEDURE SelectBrandsSentiment(In Brand text)
BEGIN
    SELECT reviews.sno, reviews.asin, reviews.cleaned_review_text
    FROM brands, reviews
    where brands.brand_id = reviews.brand_id
    AND reviews.cleaned_review_text is NOT NULL
    AND brands.Brand_Id = Brand;
end;

CREATE PROCEDURE updateSentimentScore(IN rowNum text, In Score float)
BEGIN
    UPDATE reviews
    set sentiment_score = Score
    Where reviews.sno = rowNum;
end;


CREATE PROCEDURE getBrandReviews(IN brandName text)
BEGIN
    SELECT reviews.cleaned_review_text
    FROM reviews, brands
    Where brands.Brand_Id = reviews.Brand_Id
    AND brands.Brand_name = brandName;
end;


