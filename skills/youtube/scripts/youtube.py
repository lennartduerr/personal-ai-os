#!/usr/bin/env python3
"""youtube — fetch a video transcript (direct, with optional Apify fallback).

SCAFFOLD: CLI + flow are laid out; fill in the two fetch paths where marked TODO.
"""
import argparse
import os
import re
import sys


def _video_id(url: str) -> str:
    m = re.search(r"(?:v=|youtu\.be/|/shorts/)([A-Za-z0-9_-]{11})", url)
    if not m:
        sys.exit("Could not parse a YouTube video id from the URL.")
    return m.group(1)


def transcript_direct(video_id: str):
    # TODO: use youtube-transcript-api, e.g.:
    #   from youtube_transcript_api import YouTubeTranscriptApi
    #   parts = YouTubeTranscriptApi.get_transcript(video_id)
    #   return " ".join(p["text"] for p in parts)
    raise NotImplementedError("TODO: direct transcript via youtube-transcript-api.")


def transcript_apify(video_id: str):
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        return None
    # TODO: call an Apify YouTube transcript actor with the token and return the text.
    raise NotImplementedError("TODO: Apify fallback.")


def main():
    ap = argparse.ArgumentParser(description="youtube transcript skill")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pt = sub.add_parser("transcript")
    pt.add_argument("--url", required=True)
    args = ap.parse_args()

    vid = _video_id(args.url)
    try:
        text = transcript_direct(vid)
    except Exception:
        text = transcript_apify(vid)
    if not text:
        sys.exit("No transcript available (direct + fallback failed).")
    print(text)


if __name__ == "__main__":
    main()
