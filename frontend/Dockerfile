FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

RUN npm init -y

COPY . .

EXPOSE 3000
CMD ["node", "server.js"]
