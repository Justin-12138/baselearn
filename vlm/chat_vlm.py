import base64
from openai import OpenAI

prompt = """请扮演一名数据分析专家。
1. 详细描述图片整体及每个子图的主要信息。
2. 提取各子图的核心数据关系。
3. 用 **Mermaid 语法** 输出相应可视化（如流程图、柱状图或关系图），格式如下,一定要用 ```mermaid ``` 包裹：:
   ```mermaid
    graph TD
    A-B
    ```
4. 确保每个 Mermaid 图都能表达该子图的主要信息或数据流向。"""

# client = OpenAI(base_url="http://101.52.216.165:8091/v1",api_key="None")
# model_name="qwen3-vl-30b-a3b"

client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key="AIzaSyDgnazFCrIFo0gi64CX5lwadP-ne0Schyo")
model_name="gemini-2.5-pro"

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def process_image(image_path):
    try:
        base64_image = encode_image_to_base64(image_path)
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "图中在60token的时候使用kv_cache所花的时间为什么比80token还多？"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ]
            # temperature=0.8,
            # top_p=0.8,
            # max_tokens=512
        )
        # print(response.choices[0].message.content)
        return image_path, response.choices[0].message.content
    except Exception as e:
        return image_path, f"Error: {e}"
    
# chat_vlm("请描述这张图片的内容","")
res = process_image("/home/lz/repo/baselearn/llm/infra/kv_cache_comparison.png")
print(res)