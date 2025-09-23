FROM python:3.13.7-alpine

WORKDIR /app

# gcc: C compiler required by psutil and other C extension
# musl-dev header for musl, standard C lib for alpine linux
# texlive-full: Full LaTeX distribution for PDF conversions via nbconvert
RUN apk add --no-cache gcc musl-dev linux-headers texlive-full && \
    pip install jupyter

EXPOSE 8889

# ENV NAME=World

# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8889", "--no-browser", "--allow-root"]