---creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER remove_item
AFTER INSERT
ON orders
BEGIN
    UPDATE items SET quantity = quantity - NEW.number;
END;