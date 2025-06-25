

CREATE PROCEDURE SelectAllBrands()
BEGIN
    Select brand_id, brand_name from sentiment_analysis.brands order by brand_id;
end;