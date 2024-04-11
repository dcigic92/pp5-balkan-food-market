## Setup

1. **Clone the repository:**

   ```bash
   git clone git@github.com:dcigic92/pp5-balkan-food-market.git
   ```

2. **Install dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Generate migrations:**

   ```bash
   python3 manage.py makemigrrations
   ```

4. **Apply migrations:**

   ```bash
   python3 manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python3 manage.py createsuperuser
   ```

   Follow the prompts to create an admin account.

6. **Run the development server:**

   ```bash
   python3 manage.py runserver
   ```

   The project should now be accessible at http://127.0.0.1:8000/.


## Deployment

### Heroku:

1. **Create Heroku App:**
   - Create a new Heroku app and link it to the Git repository for the project.

2. **Heroku Configurations:**
   - In Heroku's settings set up config vars such as the Database URL, Cloudinary URL and the Secret Key.

3. **Deployment:**
   - Deploy the project to Heroku by pushing the code to the Heroku remote repository, set Debug=False before final deployment.


## Testing

### Validation

- CSS validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
- HTML validated with [W3C HTML5 Validator](https://validator.w3.org/).
- JavaScript was tested with [JSHint](https://jshint.com/).
- Python has been validated using the [PEP8 Python Checker](https://www.pythonchecker.com/).

### Manual Testing

#### Account Registration
| Test |Result |
|--|--|
| User can register an account|Pass|
| User can log in|Pass|
| User can log out|Pass|
---

#### Navigation
| Test |Result |
|--|--|
|User can choose by categories|Pass|
|User can use search bar|Pass|
|User can open about page|Pass|
|User can open open newsletter page|Pass|
|User can open open home page|Pass|
|User can open open my account|Pass|
|User can open open cart|Pass|
---

#### Checkout
| Test |Result |
|--|--|
|User can process order|Pass|
|User can save informations from checkout form|Pass|
|User can see processed orders in profile history|Pass|
---

#### CRUD
| Test |Result |
|--|--|
|User can view products|Pass|
|User can rate products|Pass|
|User can remove ratings|Pass|
|User can add products to cart|Pass|
|User can view products in cart|Pass|
|User can update products in cart|Pass|
|User can remove products from cart|Pass|
|SuperUser can view products|Pass|
|SuperUser can add products|Pass|
|SuperUser can edit products|Pass|
|SuperUser can delete products|Pass|
---

#### NEWSLETTER
| Test |Result |
|--|--|
|User can subscribe to newsletter|Pass|
---

## Credits

### Code
  
- Some parts of the code were inspired by Project Boutique Ado from [Code institute](https://learn.codeinstitute.net/dashboard).

## Acknowledgements

- My mentor **Akshat Garg** for his feedback and advice.
- Our cohort facilitator **Alan Bushell**, our new cohort facilitator **Marko** and slack community.
- My wife and friends for help with testing.