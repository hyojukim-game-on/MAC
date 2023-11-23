import openai

openai.api_key = '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'

description = 'Envision two animated, passionate Asian women in their late twenties, collaborating in a classroom setting to build a movie recommendation page. The cartoon should depict the dynamic duo amidst a collection of vibrant movie posters and illuminated computer screens. Capture the essence of their enthusiastic exchange of ideas in the lively classroom atmosphere. The setting includes a cozy, dimly lit room with a cinematic ambiance, highlighting the creative process. This cartoon will serve as the ideal background for a PowerPoint presentation showcasing their movie recommendation page project.'

response = openai.images.generate(
    model="dall-e-3",
    prompt=description,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)