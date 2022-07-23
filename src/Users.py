class Users:
    def __init__(self, _id, index, guid, isActive, balance, picture, age, eyeColor,
                 name, gender, company, email, phone, address, about, registered, latitude, longitude,
                 tags, friends, greeting, favoriteFruit):
        self._id = _id
        self.index = index
        self.guid = guid
        self.isActive = isActive
        self.balance = balance
        self.picture = picture
        self.age = age
        self.eyeColor = eyeColor
        self.name = name
        self.gender = gender
        self.company = company
        self.email = email
        self.phone = phone
        self.address = address
        self.about = about
        self.registered = registered
        self.latitude = latitude
        self.longitude = longitude
        self.tags = [tags]
        self.friends = [friends]
        self.greeting = greeting
        self.favoriteFruit = favoriteFruit
