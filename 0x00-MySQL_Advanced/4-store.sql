-- create a trigger to reduce the number of items in store
CREATE TRIGGER after_order AFTER INSERT
ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name
