-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS update_item_quantity;

-- Create the trigger
CREATE TRIGGER update_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity in the items table based on the new order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
