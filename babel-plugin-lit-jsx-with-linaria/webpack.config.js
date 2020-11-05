const path = require("path");

const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  target: "web",
  entry: {
    profile: "./src/app.tsx",
  },
  output: {
    path: path.join(__dirname, "dist"),
    filename: "[name].js",
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".jsx"],
    modules: ["node_modules"]
  },
  devServer: {
    contentBase: path.join(__dirname, "dist"),
    port: 8080,
    host: `localhost`,
  },
  module: {
    rules: [
      {
        test: /\.ts(x?)$/,
        use: ["babel-loader", "linaria/loader", "ts-loader"],
      },
      {
        test: /\.js(x?)$/,
        use: ["babel-loader"],
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "styles.css",
    }),
  ],
};
