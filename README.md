# 🔐 Password Strength Checker & Generator

A Python-based cybersecurity tool that analyzes password strength and generates secure random passwords. This project demonstrates fundamental password security concepts and helps users create stronger passwords.

## 📋 Overview

This tool provides two main features:
1. **Password Strength Analysis** - Evaluates password security based on multiple criteria
2. **Secure Password Generation** - Creates cryptographically random passwords

## ✨ Features

### Password Strength Checker
- ✅ Analyzes password length and complexity
- ✅ Checks against common password databases
- ✅ Evaluates character variety (uppercase, lowercase, numbers, symbols)
- ✅ Provides color-coded strength ratings (🔴 Weak, 🟡 Medium, 🟢 Strong)
- ✅ Estimates time to crack using brute-force attacks

### Password Generator
- ✅ Generates cryptographically secure random passwords
- ✅ Customizable password length
- ✅ Includes mix of uppercase, lowercase, numbers, and special characters
- ✅ Automatically analyzes generated password strength

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation

1. Clone this repository or download the files:
```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

2. No additional dependencies required - uses Python standard library only!

### Usage

Run the program:
```bash
python password_checker.py
```

Follow the interactive menu:
1. **Check a password** - Enter any password to analyze its strength
2. **Generate a password** - Create a secure random password
3. **Exit** - Close the program

## 💡 Examples

### Example 1: Checking a Weak Password
```
Enter your password: password123

Password Strength: 🔴 Weak (common password)
Estimated time to crack: ⚠️ 0.52 seconds
```

### Example 2: Checking a Strong Password
```
Enter your password: MyS3cur3P@ssw0rd!

Password Strength: 🟢 Strong
Estimated time to crack: 🔒 2.3e+15 years
```

### Example 3: Generating a Password
```
Enter desired password length (default 12): 16

✅ Generated password: K9#mL@pQ2xR$nF7v
Password Strength: 🟢 Strong
Estimated time to crack: 🔒 8.7e+18 years
```

## 🔍 How It Works

### Strength Analysis Criteria

The tool evaluates passwords based on:

1. **Length**
   - Less than 6 characters: Weak
   - 6-7 characters: Medium
   - 8+ characters with complexity: Strong

2. **Character Variety**
   - Lowercase letters (a-z)
   - Uppercase letters (A-Z)
   - Numbers (0-9)
   - Special characters (!@#$%^&*, etc.)

3. **Common Password Check**
   - Compares against list of frequently used passwords
   - Automatically flags common passwords as weak

4. **Crack Time Estimation**
   - Calculates possible combinations based on character types
   - Assumes 1 billion attempts per second (modern GPU capability)
   - Provides realistic time estimates from seconds to years

## 🎯 Password Security Best Practices

Based on this tool, here are key recommendations:

✅ **Use at least 12 characters** - Longer is always better  
✅ **Mix character types** - Combine uppercase, lowercase, numbers, and symbols  
✅ **Avoid common passwords** - Never use "password123", "qwerty", etc.  
✅ **Use unique passwords** - Different password for each account  
✅ **Consider a password manager** - Safely store complex passwords  

## 🛡️ Security Considerations

### Why Password Strength Matters

- **Weak passwords** can be cracked in seconds or minutes
- **Strong passwords** can take millions of years to crack with current technology
- Most security breaches involve compromised passwords

### Limitations

⚠️ **Important Notes:**
- This tool is for **educational purposes**
- Crack time estimates assume brute-force attacks only
- Real-world attacks may use dictionary attacks or other methods
- Always use additional security measures (2FA, biometrics, etc.)

## 🔧 Technical Details

### Built With
- **Python 3.x** - Core programming language
- **Standard Library Modules:**
  - `random` - Secure password generation
  - `string` - Character set definitions

### Algorithm Overview

1. **Password Analysis**
   - Iterates through password characters
   - Checks for character type presence
   - Compares against common password list
   - Calculates strength score

2. **Crack Time Calculation**
   ```
   Combinations = charset_size ^ password_length
   Time (seconds) = Combinations / Guesses_per_second
   ```

3. **Password Generation**
   - Uses Python's `random.choice()` for randomization
   - Ensures all character types are included
   - Shuffles result for unpredictability

## 📚 Learn More

### Resources
- [OWASP Password Guidelines](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [NIST Password Standards](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [How Secure Is My Password?](https://www.security.org/how-secure-is-my-password/)

## 🤝 Contributing

Contributions are welcome! Here are ways you can help:

- Report bugs or issues
- Suggest new features
- Improve documentation
- Submit pull requests

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

Created as a cybersecurity learning project to demonstrate password security concepts and Python programming skills.

## 🙏 Acknowledgments

- Inspired by real-world password security challenges
- Built to help raise awareness about password hygiene
- Thanks to the cybersecurity community for best practices

---

## 📞 Contact

Feel free to reach out with questions, suggestions, or feedback!

**⚠️ Disclaimer:** This tool is for educational purposes only. Always follow your organization's security policies and use approved tools for production environments.

---

**Stay secure! 🔒**
