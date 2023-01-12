---creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER remove_item
AFTER INSERT
ON orders
BEGIN
    SET @num_items = SELECT quantity FROM items WHERE name = NEW.item_name;
    IF num_items > 0 THEN
        UPDATE items SET quantity = quantity - NEW.number;
    ELSE
        UPDATE items SET quantity = 0;
    END IF
END;