# MongoDB Commands for FastAPI Docker Project

## 1. Enter MongoDB Container

```bash
docker exec -it <container_id> mongosh
```

## 2. Select Database

```javascript
use fastapi_db
```

## 3. Show All Databases

```javascript
show dbs
```

## 4. Show Current Database

```javascript
db
```

## 5. Show Collections

```javascript
show collections
```

## 6. Show All Records

```javascript
db.items.find().pretty()
```

## 7. Show One Record

```javascript
db.items.findOne()
```

## 8. Count Records

```javascript
db.items.countDocuments()
```

## 9. Insert One Record

```javascript
db.items.insertOne({
  name: "Keyboard",
  description: "Mechanical keyboard",
  price: 2500
})
```

## 10. Insert Multiple Records

```javascript
db.items.insertMany([
  {
    name: "Laptop",
    description: "Student laptop",
    price: 45000
  },
  {
    name: "Mouse",
    description: "Wireless mouse",
    price: 800
  }
])
```

## 11. Find a Specific Item

```javascript
db.items.find({
  name: "Laptop"
}).pretty()
```

## 12. Find Items with Price Greater Than 1000

```javascript
db.items.find({
  price: { $gt: 1000 }
}).pretty()
```

## 13. Update a Record

```javascript
db.items.updateOne(
  { name: "Laptop" },
  { $set: { price: 42000 } }
)
```

## 14. Update Multiple Records

```javascript
db.items.updateMany(
  { price: { $lt: 1000 } },
  { $set: { category: "Budget" } }
)
```

## 15. Delete One Record

```javascript
db.items.deleteOne({
  name: "Mouse"
})
```

## 16. Delete Multiple Records

```javascript
db.items.deleteMany({
  price: { $lt: 1000 }
})
```

## 17. Show Database Statistics

```javascript
db.stats()
```

## 18. Show Collection Statistics

```javascript
db.items.stats()
```

## 19. Sort Items by Price

### Ascending Order

```javascript
db.items.find().sort({
  price: 1
}).pretty()
```

### Descending Order

```javascript
db.items.find().sort({
  price: -1
}).pretty()
```

## 20. Limit Results

```javascript
db.items.find().limit(2).pretty()
```

## 21. Exit MongoDB Shell

```javascript
exit
```

---


