DESCryptoServiceProvider cryptic = new DESCryptoServiceProvider(); 
cryptic.Key = ASCIIEncoding.ASCII.GetBytes("ABCDEFGH"); 
cryptic.IV = ASCIIEncoding.ASCII.GetBytes("ABCDEFGH"); 
cryptic.Mode = CipherMode.CBC;
FileStream stream = new FileStream(@"d:\test.txt", FileMode.OpenOrCreate,FileAccess.Write)
CryptoStream crStream = new CryptoStream(fs, cryptic.CreateEncryptor(),CryptoStreamMode.Write);
byte[] data = ASCIIEncoding.ASCII.GetBytes("Hello World!");
crStream.Write(data, 0, data.Length);
crStream.Close();
fs.Close();






DESCryptoServiceProvider cryptic = new DESCryptoServiceProvider(); 
cryptic.Key = ASCIIEncoding.ASCII.GetBytes("ABCDEFGH"); 
cryptic.IV = ASCIIEncoding.ASCII.GetBytes("ABCDEFGH"); 
cryptic.Mode = CipherMode.CBC;
FileStream stream = new FileStream(@"d:\test.txt", FileMode.Open,FileAccess.Read);
CryptoStream crStream = new CryptoStream(stream, cryptic.CreateDecryptor(), CryptoStreamMode.Read);
StreamReader reader = new StreamReader(crStream); 
string data = reader.ReadToEnd();
reader.Close(); 
stream.Close();