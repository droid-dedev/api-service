// types.ts

// Importing required types
import { Request, Response } from 'express';

// Defining custom types
export type RequestBody<T> = T & {
  [P in keyof T]?: T[P];
};

export type ResponseBody<T> = {
  [P in keyof T]?: T[P];
};

export type ApiError = {
  statusCode: number;
  message: string;
};

export type User = {
  id: string;
  name: string;
  email: string;
};

export type Product = {
  id: string;
  name: string;
  price: number;
};

export type CartItem = {
  id: string;
  quantity: number;
  product: Product;
};

export type Order = {
  id: string;
  userId: string;
  items: CartItem[];
};