#!/usr/bin/env python3
"""
Helper script to create a new challenge folder with template files.

Usage:
    python create_challenge.py "Challenge_Name" [points] [category]

Example:
    python create_challenge.py "Keyed_Permutations" 50 "Beginner"
"""

import os
import sys
from pathlib import Path

SOLUTION_TEMPLATE = '''"""
Challenge: {challenge_name}
Points: {points}
Category: {category}
Link: https://cryptohack.org/challenges/{url}/

Description:
[Brief description of the challenge]

Approach:
[Explain your approach to solving this challenge]
"""

# Your solution code here

def solve():
    """
    Main solution function
    """
    pass

if __name__ == "__main__":
    result = solve()
    print(f"Result: {{result}}")
'''

README_TEMPLATE = '''# {challenge_name}

**Points:** {points}  
**Category:** {category}  
**Link:** https://cryptohack.org/challenges/{url}/

## Challenge Description

[Paste or describe the challenge here]

## Solution Approach

[Explain your approach and methodology]

## Key Concepts

- Concept 1
- Concept 2

## Running the Solution

```bash
python solution.py
```

## Result

```
[Expected output or flag]
```

## Notes

[Any additional notes, resources, or insights]
'''

def create_challenge(challenge_name, points="XX", category="Beginner"):
    """Create a new challenge folder with template files."""
    
    # Get the script's directory (project root)
    project_root = Path(__file__).parent
    
    # Create challenge folder
    challenge_folder = project_root / challenge_name
    
    if challenge_folder.exists():
        print(f"❌ Error: Folder '{challenge_name}' already exists!")
        return False
    
    challenge_folder.mkdir(parents=True, exist_ok=True)
    
    # Generate URL-friendly name
    url_name = challenge_name.lower().replace('_', '-')
    
    # Create solution.py
    solution_file = challenge_folder / "solution.py"
    solution_file.write_text(SOLUTION_TEMPLATE.format(
        challenge_name=challenge_name.replace('_', ' '),
        points=points,
        category=category,
        url=url_name
    ))
    
    # Create README.md
    readme_file = challenge_folder / "README.md"
    readme_file.write_text(README_TEMPLATE.format(
        challenge_name=challenge_name.replace('_', ' '),
        points=points,
        category=category,
        url=url_name
    ))
    
    print(f"✅ Created challenge folder: {challenge_name}/")
    print(f"   - solution.py")
    print(f"   - README.md")
    print(f"\nNext steps:")
    print(f"1. cd {challenge_name}")
    print(f"2. Edit solution.py with your code")
    print(f"3. Update README.md with challenge details")
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_challenge.py <Challenge_Name> [points] [category]")
        print("\nExample:")
        print("  python create_challenge.py Keyed_Permutations 50 Beginner")
        sys.exit(1)
    
    challenge_name = sys.argv[1]
    points = sys.argv[2] if len(sys.argv) > 2 else "XX"
    category = sys.argv[3] if len(sys.argv) > 3 else "Beginner"
    
    create_challenge(challenge_name, points, category)

if __name__ == "__main__":
    main()
