FROM python:3.12-slim

WORKDIR /app

COPY html/ ./html/

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.requesr.urlopen('http://localhost:8080')" || exit 1

CMD [\"python3\", \"-m\", \"http.server\", \"8080\", \"--directory\", \"html\"]
