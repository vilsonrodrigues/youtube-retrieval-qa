def youtube_doc_loader(url: str) -> List:
    from langchain.document_loaders import YoutubeLoader
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
    data = loader.load()
    return data