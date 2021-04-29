-- dummy comment dummy comment dummy comment
-- dummy comment dummy comment dummy comment
CREATE TRIGGER remove_item
AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name;
