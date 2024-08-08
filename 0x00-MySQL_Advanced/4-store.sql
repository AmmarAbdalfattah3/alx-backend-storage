-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS decrease_quantity_after_order;
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
