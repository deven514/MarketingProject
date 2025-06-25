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
    Select products.title, reviews.rating, reviews.cleaned_review_text from products, reviews
    Where reviews.asin = products.asin
    and reviews.asin = amazonNo;
END;

CREATE PROCEDURE SelectByBrand(In brand text)
BEGIN
    SELECT asin, rating, cleaned_review_text from reviews, brands
    WHERE brands.Brand_Id = reviews.Brand_Id
    AND brands.brand_name = brand
    AND cleaned_review_text is NOT NULL
    ORDER BY asin;
end;


CREATE PROCEDURE SelectAllBrandNames()
BEGIN
    Select brand_name from brands order by brand_name;
end;
