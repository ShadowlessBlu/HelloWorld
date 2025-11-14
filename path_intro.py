from pathlib import Path

path = Path("emails")

print(path.exists())
print(path.mkdir())
print(path.rmdir())

path = Path()

for file in path.glob('*'):
    print(file)


