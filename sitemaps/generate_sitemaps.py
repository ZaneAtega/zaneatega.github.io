with open('github.io.xml', 'r', encoding='utf-8') as file: content = file.read()

replacements = ['pages.dev','vercel.app','onrender.com','netlify.app']

for replacement in replacements:
    with open(replacement + '.xml', 'w', encoding='utf-8') as file:
        file.write(content.replace('github.io',replacement))