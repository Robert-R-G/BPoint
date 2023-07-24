import re

def paragraph_to_bullet_points(paragraph):
    # Split the paragraph into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)
    
    # Create bullet points
    bullet_points = ['• {}'.format(sentence) for sentence in sentences]
    
    bullet_points_paragraph = '\n'.join(bullet_points)
    
    return bullet_points_paragraph

paragraph = input('Paste paragraph here: ')
print('')
bullet_points = paragraph_to_bullet_points(paragraph)
print(bullet_points)